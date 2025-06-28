# Social Media Clone

## Overview

This is a Flask-based social media application that provides core social networking features including user authentication, posting, following, and engagement through likes and comments. The application uses a traditional MVC architecture with server-side rendering and follows Flask best practices.

## System Architecture

### Backend Architecture
- **Framework**: Flask web framework with SQLAlchemy ORM
- **Database**: SQLite (development) with PostgreSQL support via environment configuration
- **Authentication**: Session-based authentication using Flask sessions
- **Forms**: Flask-WTF for form handling and validation
- **Templates**: Jinja2 templating engine with Bootstrap 5 for responsive UI

### Frontend Architecture
- **Styling**: Bootstrap 5 with custom CSS
- **Theme**: Dark theme implementation
- **Icons**: Bootstrap Icons
- **JavaScript**: Vanilla JavaScript for interactive features
- **Responsive Design**: Mobile-first approach using Bootstrap grid system

## Key Components

### Models (models.py)
- **User Model**: Handles user accounts, authentication, and follower relationships
- **Post Model**: Manages user posts and content
- **Comment Model**: Handles post comments
- **Like Model**: Manages post likes
- **Association Tables**: Many-to-many relationship for followers

### Forms (forms.py)
- **LoginForm**: User authentication
- **RegistrationForm**: New user registration with validation
- **PostForm**: Content creation
- **CommentForm**: Comment submission
- **EditProfileForm**: Profile management

### Routes (routes.py)
- Authentication routes (login, register, logout)
- Social features (feed, posts, profile, follow/unfollow)
- Content management (create, like, comment)
- Profile management

### Templates
- **Base template**: Consistent navigation and layout
- **Authentication pages**: Login and registration
- **Social pages**: Feed, profile, individual posts
- **Responsive design**: Mobile-optimized layouts

## Data Flow

1. **User Registration/Login**: Users register with username/email/password, sessions maintain authentication state
2. **Content Creation**: Authenticated users create posts through forms with validation
3. **Social Interaction**: Users can follow others, like posts, and add comments
4. **Feed Generation**: Personalized feed shows posts from followed users
5. **Profile Management**: Users can edit their profiles and view others' profiles

## External Dependencies

### Python Packages
- Flask: Web framework
- Flask-SQLAlchemy: Database ORM
- Flask-WTF: Form handling
- WTForms: Form validation
- Werkzeug: Password hashing and security utilities

### Frontend Dependencies
- Bootstrap 5: CSS framework (CDN)
- Bootstrap Icons: Icon library (CDN)
- Custom CSS/JS: Application-specific styling and behavior

### Database
- SQLite: Default development database
- PostgreSQL: Production database support (configurable via DATABASE_URL)

## Deployment Strategy

- **Development**: Local Flask development server with SQLite
- **Production**: Configurable database URL for PostgreSQL deployment
- **Security**: Environment-based secret key configuration
- **Proxy Support**: ProxyFix middleware for reverse proxy deployments
- **Session Management**: Persistent sessions with configurable secret

## Changelog

```
Changelog:
- June 28, 2025. Initial setup
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```