import axios from 'axios';
import { API_URL } from '../../config';


const REGISTER_URL = `${API_URL}/users/`;
const LOGIN_URL = `${API_URL}/auth/jwt/create/`;
const ACTIVATE_URL = `${API_URL}/auth/users/activation/`;


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

    if (response.data) {
        localStorage.setItem("user", JSON.stringify(response.data))
    }

    return response.data;
};


const logout = () => localStorage.removeItem("user");


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