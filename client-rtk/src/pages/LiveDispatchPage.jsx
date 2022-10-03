import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Table } from 'react-bootstrap';
import Spinner from '../components/Spinner';
import {toast} from 'react-toastify';
import { getMyDispatches, reset } from '../features/mydispatches/myDispatchSlice'
// import MyDispacthListView from '../components/MyDispacthListView';


const LiveDispatchPage = () => {

    const { mydispatchelists, isLoading, isError, isSuccess, message } = useSelector((state) => state.myDispatches);

    const dispatch = useDispatch();

    useEffect(() => {
        if (isError) {
            toast.error(message, {icon: "😜"});
        }
        dispatch(getMyDispatches());
    }, [dispatch, isError, message]);

    if (isLoading) {
        return <Spinner />;
    };

    // const numberWithCommas = (x) => {
    //     return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    // };

    // const date = new Date("2020-07-22T13:22:10.2566789+00:00");

    // const customDate = (x) => {
    //     const formattedDate = x.toLocaleDateString("en-GB", {
    //         day: "numeric",
    //         month: "numeric",
    //         year: "numeric"
    //     });
    //     return formattedDate;
    // }

    const newCustDateTime = (x) => {
        const formatDateTime = new Intl.DateTimeFormat('en-GB', { 
            dateStyle: 'medium', 
            timeStyle: 'short' 
        }).format(x);

        return formatDateTime;
    }

    // console.log(formattedDate);

    return (
        <>
            <div className="p-5">
            {/* <Container> */}
                <br />
                <br />
                <h1 className="justify-content-center align-content-center text-center">
                    Yantrayug Dispatch List
                </h1>
                <br />
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>Sr. No.</th>
                            <th>Entry Date</th>
                            <th>Party Name</th>
                            <th>Product</th>
                            {/* <th>Price</th> */}
                            <th>Pick List</th>
                            <th>Invoice No.</th>
                            <th>Bill Status</th>
                            <th>Delivery By</th>
                            <th>Delivery Date</th>
                            <th>Pickers</th>
                            <th>Dispatch Status</th>
                            <th>Recieved Status</th>
                            <th>Remark</th>
                        </tr>
                    </thead>
                    {
                        <>
                        <tbody>
                        {mydispatchelists.map((mdlist) => (
                            <tr>
                                <td>{mdlist.pkid}</td>
                                <td>
                                    {newCustDateTime(new Date(mdlist.created_at))}
                                </td>
                                <td>{mdlist.party_name}</td>
                                <td>{mdlist.product}</td>
                                {/* <td>
                                    ₹{numberWithCommas(Number(mdlist.total_price))}
                                </td> */}
                                <td>{mdlist.pick_list}</td>
                                <td>{mdlist.invoice_no}</td>
                                <td>{mdlist.bill_status}</td>
                                <td>{mdlist.delivered_man.user.first_name}</td>
                                <td>
                                    {newCustDateTime(new Date(mdlist.delivery_date))}
                                </td>
                                <td>{mdlist.picker_name.user.first_name}</td>
                                <td>{mdlist.dispatch_status}</td>
                                <td>{mdlist.recieved_status}</td>
                                <td>{mdlist.remark}</td>
                                {/* <td>
                                    {newCustDateTime(new Date(mdlist.delivery_date))}
                                </td> */}
                            </tr>
                        ))}
                        </tbody>
                        </>
                    }
                </Table>
            {/* </Container> */}
            </div>
        </>
    )
}

export default LiveDispatchPage