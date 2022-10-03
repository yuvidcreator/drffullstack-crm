import axios from 'axios';
import { API_URL } from '../../config'


const getMyDispatches = async () => {

    // const API_URL = "http://127.0.0.1:8080"
    
    const response = await axios.get(`${API_URL}/dispatch/`);
    // const response = await axios.get("http://127.0.0.1:8000/api/v1/dispatch/");
    // console.log(response.data);
    return response.data
}

const myDispatchAPIService = {getMyDispatches};

export default myDispatchAPIService;