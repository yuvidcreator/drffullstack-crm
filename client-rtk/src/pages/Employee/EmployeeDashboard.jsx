import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
// // import { Table } from 'react-bootstrap';
import Spinner from '../../components/Spinner';
import {toast} from 'react-toastify';
// import { getDeliveryBoyDispatchList } from '../features/deliveryboydispatches/DeliveryBoyDispatchSlice'
import { reset } from '../../features/auth/authSlice'




const EmployeeDashboard = () => {

    // const { deliveryboydispatchelists, isLoading, isError, message } = useSelector((state) => state.DeliveryBoyDispatches);
    const { user, userToken, isLoading, isError, message } = useSelector((state) => state.auth);

    const dispatch = useDispatch();

    console.log(userToken);

    useEffect(() => {
        if (isError) {
            toast.error(message, {icon: "😜"});
        } 

        dispatch(reset());

    }, [dispatch, user, userToken, isError, message]);

    if (isLoading) {
        return <Spinner />;
    } 

    const newCustDateTime = (x) => {
        const formatDateTime = new Intl.DateTimeFormat('en-GB', { 
            dateStyle: 'medium', 
            timeStyle: 'short' 
        }).format(x);

        const numberWithCommas = (x) => {
            return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        };

        return formatDateTime;
    }

    console.log(user);

    return (
        <div>
            <br />
            <br />
            <br />
            <br />
            {/* {user.first_name}'s' EmployeeDashboard */}
            <h2 className="justify-content-center align-content-center text-center">EmployeeDashboard</h2>
            <>
            <div className="p-2">
            {/* <Container> */}
                <br />
                <br />
                <h1 className="justify-content-center align-content-center text-center">
                    Delivery Boy Dispatch List
                </h1>
                {/* <p>{user}</p> */}
                <br />
                {/* <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>Sr. No.</th>
                            <th>Dispatch Order ID</th>
                            <th>invoice_no</th>
                            <th>Party Name</th>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Bill Status</th>
                            <th>Assigned Person</th>
                            <th>Delivery Date</th>
                            <th>Pickers</th>
                            <th>Dispatch Status</th>
                            <th>Recieved Status</th>
                            <th>Payment Method</th>
                            <th>Remark</th>
                        </tr>
                    </thead>
                    {
                        <>
                        <tbody>
                        {deliveryboydispatchelists.map((mdlist) => (
                            <tr key={mdlist.id}>
                                <td>{mdlist.pkid}</td>
                                <td>{mdlist.dispatch_order_id}</td>
                                <td>{mdlist.invoice_no}</td>
                                <td>{mdlist.party_name}</td>
                                <td>{mdlist.product}</td>
                                <td>
                                    ₹{(mdlist.total_price)}
                                </td>
                                <td>{mdlist.bill_status}</td>
                                <td>{mdlist.delivered_man.user.first_name}</td>
                                <td>
                                    {newCustDateTime(new Date(mdlist.created_at))}
                                </td>
                                <td>
                                    ₹{numberWithCommas(Number(mdlist.total_price))}
                                </td>
                                <td>{mdlist.pick_list}</td>
                                <td>
                                    {newCustDateTime(new Date(mdlist.delivery_date))}
                                </td>
                                <td>{mdlist.picker_name.user.first_name}</td>
                                <td>{mdlist.dispatch_status}</td>
                                <td>{mdlist.recieved_status}</td>
                                <td>{mdlist.payment_method}</td>
                                <td>{mdlist.remark}</td>
                                <td>
                                    {newCustDateTime(new Date(mdlist.delivery_date))}
                                </td>
                            </tr>
                        ))}
                        </tbody>
                        </>
                    }
                </Table> */}
            {/* </Container> */}
            </div>
            </>
        </div>
    )
};

export default EmployeeDashboard;