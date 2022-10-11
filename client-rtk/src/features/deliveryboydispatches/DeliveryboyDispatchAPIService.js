import axios from 'axios';
import { API_URL } from '../../config'


const getDeliveryBoyDispatchList = async () => {

    // const API_URL = "http://127.0.0.1:8080"
    
    const response = await axios.get(`${API_URL}/dispatch/delivery_boy_dispatchlist`);
    // const response = await axios.get("http://127.0.0.1:8000/api/v1/dispatch/");
    // console.log(response.data);
    return response.data
}

const DeliveryBoyDispatchAPIService = {getDeliveryBoyDispatchList};

export default DeliveryBoyDispatchAPIService;