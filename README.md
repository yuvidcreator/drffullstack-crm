# Django Backend API

# Django Djoser endpoints 
# Available endpoints
# Token based --> 
/api/token/
/api/token/refresh/
/api/token/verify/

# djoser --> /api/v1/auth/
/users/
/users/me/          (GET, PUT, PATCH)
/users/confirm/
/users/set_password/
/users/reset_password/
/users/reset_password_confirm/
/users/set_username/
/users/reset_username/
/users/reset_username_confirm/
/token/login/       (Token Based Authentication)
/token/logout/      (Token Based Authentication)
/jwt/create/        (JSON Web Token Authentication)
/jwt/refresh/       (JSON Web Token Authentication)
/jwt/verify/        (JSON Web Token Authentication)


/users/activation/{uid}/{token}
/users/resend_activation/{uid}/{token}