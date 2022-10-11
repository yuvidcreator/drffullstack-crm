import axios from 'axios';
// import { API_URL } from '../../config';


// const REGISTER_URL = `${API_URL}/v1/auth/users/`;
// const LOGIN_URL = `${API_URL}/auth/jwt/create/`;
// const ACTIVATE_URL = `${API_URL}/v1/auth/users/activation/`;
// const USER_URL = `${API_URL}/v1/auth/users/me/`


const REGISTER_URL = "/api/v1/auth/users/";
const ACTIVATE_URL = "/api/v1/auth/users/resend_activation/";
const RESEND_EMAIL_ACTIVATE_URL = "/api/v1/auth/users/activation/";
const LOGIN_URL = "/api/v1/auth/jwt/create/";
// const AUTH_LOGIN = "/api/token/";
const USER_URL = "/api/v1/auth/users/me/";
const EMPLOYEE_PROFILE_URL = "/api/v1/profiles/employee/";


// Registering User --> He/She may be Employee or Customer
const register = async (userData) => {
    const config = {
        headers: {
            "Content-Type": "application/json",
        }
    };

    const response = await axios.post(REGISTER_URL, userData, config);

    return response.data;
};



// Login Employee 
const login = async (userData) => {
    const config = {
        headers: {
            "Content-Type": "application/json",
        }
    };

    const response = await axios.post(LOGIN_URL, userData, config);
    
    // console.log(response.data.access);
    // console.log(response.data);

    if (response.data) {
        localStorage.setItem("userToken", JSON.stringify(response.data));
        
        const config = {
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${response.data.access}`,
            }
        };
    
        const usr_response = await axios.get(EMPLOYEE_PROFILE_URL, config);
        
        // console.log(usr_response.data);
    
        if (usr_response.data) {
            localStorage.setItem("user", JSON.stringify(usr_response.data));
        }
    
        return (usr_response.data);
    }

    return (response.data);
};


const logout = () => {localStorage.removeItem("userToken"); localStorage.removeItem("user");};


const activate = async (userData) => {
    const config = {
        headers: {
            "Content-Type": "application/json",
        }
    };

    const response = await axios.post(ACTIVATE_URL, userData, config);

    return response.data;
};


const authAPIService = { register, activate, login, logout };

export default authAPIService;