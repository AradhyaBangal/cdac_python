from flask import render_template, flash, redirect, url_for, request, session, jsonify
from app import app, db
from forms import LoginForm, RegistrationForm, PostForm, CommentForm, EditProfileForm
from models import User, Post, Comment, Like
from datetime import datetime

def login_required(f):
    """Decorator to require login for certain routes"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def get_current_user():
    """Get current logged in user"""
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None

@app.context_processor
def inject_user():
    """Make current user available in all templates"""
    return dict(current_user=get_current_user())

@app.route('/')
def index():
    current_user = get_current_user()
    if current_user:
        return redirect(url_for('feed'))
    
    # Show recent public posts for non-logged in users
    posts = Post.query.order_by(Post.created_at.desc()).limit(10).all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('feed'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            session.permanent = True
            flash(f'Welcome back, {user.username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('feed'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('feed'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/feed')
@login_required
def feed():
    current_user = get_current_user()
    form = PostForm()
    
    # Get posts from followed users and own posts
    posts = current_user.get_feed_posts().limit(50).all()
    
    return render_template('feed.html', posts=posts, form=form)

@app.route('/create_post', methods=['POST'])
@login_required
def create_post():
    current_user = get_current_user()
    form = PostForm()
    
    if form.validate_on_submit():
        post = Post(content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
    else:
        for error in form.content.errors:
            flash(f'Error: {error}', 'danger')
    
    return redirect(url_for('feed'))

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
    return render_template('post.html', post=post, comments=comments, form=form)

@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    current_user = get_current_user()
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            user_id=current_user.id,
            post_id=post_id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
    else:
        for error in form.content.errors:
            flash(f'Error: {error}', 'danger')
    
    return redirect(url_for('view_post', post_id=post_id))

@app.route('/like/<int:post_id>', methods=['POST'])
@login_required
def toggle_like(post_id):
    current_user = get_current_user()
    post = Post.query.get_or_404(post_id)
    
    existing_like = Like.query.filter_by(user_id=current_user.id, post_id=post_id).first()
    
    if existing_like:
        # Unlike the post
        db.session.delete(existing_like)
        action = 'unliked'
    else:
        # Like the post
        like = Like(user_id=current_user.id, post_id=post_id)
        db.session.add(like)
        action = 'liked'
    
    db.session.commit()
    
    # Return JSON for AJAX requests
    if request.headers.get('Content-Type') == 'application/json':
        return jsonify({
            'action': action,
            'like_count': post.like_count(),
            'is_liked': post.is_liked_by(current_user)
        })
    
    flash(f'Post {action}!', 'success')
    return redirect(request.referrer or url_for('feed'))

@app.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    current_user = get_current_user()
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.created_at.desc()).all()
    
    # Check if current user is following this user
    is_following = False
    if current_user and current_user.id != user.id:
        is_following = current_user.is_following(user)
    
    return render_template('profile.html', user=user, posts=posts, is_following=is_following)

@app.route('/follow/<username>')
@login_required
def follow(username):
    current_user = get_current_user()
    user = User.query.filter_by(username=username).first_or_404()
    
    if user == current_user:
        flash('You cannot follow yourself!', 'warning')
        return redirect(url_for('profile', username=username))
    
    current_user.follow(user)
    db.session.commit()
    flash(f'You are now following {user.username}!', 'success')
    return redirect(url_for('profile', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    current_user = get_current_user()
    user = User.query.filter_by(username=username).first_or_404()
    
    if user == current_user:
        flash('You cannot unfollow yourself!', 'warning')
        return redirect(url_for('profile', username=username))
    
    current_user.unfollow(user)
    db.session.commit()
    flash(f'You are no longer following {user.username}.', 'info')
    return redirect(url_for('profile', username=username))

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    current_user = get_current_user()
    form = EditProfileForm()
    
    if form.validate_on_submit():
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile', username=current_user.username))
    elif request.method == 'GET':
        form.bio.data = current_user.bio
    
    return render_template('edit_profile.html', form=form)

@app.route('/discover')
@login_required
def discover():
    current_user = get_current_user()
    # Show users that current user is not following
    users = User.query.filter(User.id != current_user.id).all()
    suggested_users = [user for user in users if not current_user.is_following(user)]
    return render_template('discover.html', users=suggested_users[:10])

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
