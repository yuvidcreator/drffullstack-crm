import React, {useState, useEffect} from 'react';
import {Container, Form, Button, Row, Col} from 'react-bootstrap';
import { FaUser } from 'react-icons/fa';
// import { MdOutlineAppRegistration } from 'react-icons/md';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import Spinner from '../components/Spinner';
import { register, reset, logout } from '../features/auth/authSlice';


const SignupPage = () => {

    const [email, setEmail] = useState("");
    const [first_name, setFirstName] = useState("");
    const [last_name, setLastName] = useState("");
    // const [mobile, setMobile] = useState("");
    const [is_employee, setEmployee] = useState(false);
    const [password, setPassword] = useState("");
    const [re_password, setRePassword] = useState("");

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const {userToken, isError, isLoading, isSuccess, message} = useSelector((state) => state.auth);

    useEffect(() => {
        if (isError) {
            toast.error(message);
        }

        if (isSuccess) {
            navigate("/");
            dispatch(logout());
            toast.success(
                "An activation Email has been sent to your registered email. Please check your Email."
            );
        }

        dispatch(reset());
    }, [isError, isSuccess, message, userToken, navigate, dispatch]);

    const submitHandler = (e) => {
        e.preventDefault();

        if (!email) {
            toast.error("An Email must be provided");
        }

        // if (!mobile) {
        //     toast.error("Mobile No. must be provided");
        // }

        if (!first_name) {
            toast.error("First Name must be provided");
        }

        if (!last_name) {
            toast.error("Last Name must be provided");
        }

        if (password !== re_password) {
            toast.error("Passord Not Matched, Try Again.")
        } else {
            const userData = {
                email,
                first_name,
                last_name,
                password,
                re_password,
                is_employee
            };

            console.log(userData);

            dispatch(register(userData));
        }
    };

    return (
        <>
            <br />
            <br />
            <br />
            <Container className="d-flex">
                <Container>
                    <Row>
                        <Col className="mg-top text-center">
                            <section>
                                <h1>
                                    <FaUser /> Create An Account
                                </h1>
                                <hr className="hr-text" />
                            </section>
                        </Col>
                    </Row>

                    {isLoading && <Spinner />}

                    <Row className="mt-3">
                        <Col className="justify-content-center">
                            <Form onSubmit={submitHandler}>
                                <Form.Group controlId="email">
                                    <Form.Label>Email ID</Form.Label>
                                    <Form.Control 
                                        type="email" 
                                        placeholder="Enter Email ID" 
                                        value={email} 
                                        onChange={(e)=>setEmail(e.target.value)} 
                                        required
                                    />
                                </Form.Group>
                                {/* <Form.Group controlId="mobile" className="mt-3">
                                    <Form.Label>Mobile No.</Form.Label>
                                    <Form.Control 
                                        type="mobile" 
                                        placeholder="Enter Mobile No" 
                                        value={mobile} 
                                        onChange={(e)=>setMobile(e.target.value)} 
                                    />
                                </Form.Group> */}
                                <Form.Group controlId="first_name" className="mt-3">
                                    <Form.Label>First Name</Form.Label>
                                    <Form.Control 
                                        type="name" 
                                        placeholder="Enter First Name" 
                                        value={first_name} 
                                        onChange={(e)=>setFirstName(e.target.value)} 
                                    />
                                </Form.Group>
                                <Form.Group controlId="last_name" className="mt-3">
                                    <Form.Label>Last Name</Form.Label>
                                    <Form.Control 
                                        type="name" 
                                        placeholder="Enter Last Name" 
                                        value={last_name} 
                                        onChange={(e)=>setLastName(e.target.value)} 
                                    />
                                </Form.Group>
                                <Form.Group controlId="password" className="mt-3">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control
                                        type="password" 
                                        placeholder="Enter Password" 
                                        value={password} 
                                        onChange={(e)=>setPassword(e.target.value)} 
                                        required
                                        minLength='8'
                                    />
                                </Form.Group>
                                <Form.Group controlId="re-password" className="mt-3">
                                    <Form.Label>Confirm Password</Form.Label>
                                    <Form.Control
                                        type="password" 
                                        placeholder="Enter Again Password" 
                                        value={re_password} 
                                        onChange={(e)=>setRePassword(e.target.value)} 
                                        required
                                        minLength='8'
                                    />
                                </Form.Group>
                                <Form.Group controlId="is_employee" className="mt-3">
                                    <Form.Check
                                        type="checkbox"
                                        label="Is Employee Account.??"
                                        name='is_employee'
                                        value={is_employee} 
                                        onChange={(e)=>setEmployee(e.target.checked)} 
                                    />
                                </Form.Group>
                                <Button type="submit" variant="primary" className="mt-3">
                                    Signup
                                </Button>
                            </Form>
                        </Col>
                    </Row>

                    <Row className="py-3">
                        <Col>
                            Already have an Account?
                            <Link to="/login" className="mx-2">Login Here....</Link>
                        </Col>
                    </Row>
                </Container>
            </Container>
        </>
    )
};

export default SignupPage;