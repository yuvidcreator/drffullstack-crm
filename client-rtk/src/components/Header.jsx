import React from 'react';
import { Container, Nav, Navbar, NavDropdown } from 'react-bootstrap';
// import { GiDutchBike } from 'react-icons/gi';
import { MdLogin, MdLogout, MdOutlineAppRegistration } from 'react-icons/md';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { LinkContainer } from 'react-router-bootstrap';
import { logout, reset } from '../features/auth/authSlice';


const Header = () => {

    const navigate = useNavigate();

    const dispatch = useDispatch();

    const { user } = useSelector((state)=>state.auth);

    const logoutHandler = () => {
        dispatch(logout());
        dispatch(reset());
        navigate("/");
    }

    return (
        <header>
            <Navbar fixed="top" collapseOnSelect expand="lg" bg="dark" variant="dark">
                <Container>
                    <LinkContainer to="/">
                        <Navbar.Brand>
                            Yantrayug
                            {/* <GiDutchBike className="nav-icon mx-2" /> */}
                        </Navbar.Brand>
                    </LinkContainer>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse 
                        id="responsive-navbar-nav"
                        className="justify-content-end"
                    >
                        <Nav className="me-auto">
                            <LinkContainer to="/">
                                <Nav.Link>
                                    Home
                                </Nav.Link>
                            </LinkContainer>
                            <LinkContainer to="/dispatch">
                                <Nav.Link>Dispatch</Nav.Link>
                            </LinkContainer>
                            <LinkContainer to="/employee">
                                <Nav.Link>Employee</Nav.Link>
                            </LinkContainer>

                            { user ? (
                                        <NavDropdown title={user.first_name ? user.first_name : "Welcome"} id="username">
                                            <LinkContainer to="/profile">
                                                <NavDropdown.Item>
                                                    Profile
                                                </NavDropdown.Item>
                                            </LinkContainer>
                                            <NavDropdown.Item onClick={logoutHandler}>
                                                <MdLogin /> Logout
                                            </NavDropdown.Item>
                                        </NavDropdown>
                                    ) : (
                                            <NavDropdown title="Accounts" id="collasible-nav-dropdown">
                                                <LinkContainer to="/login">
                                                    <NavDropdown.Item>
                                                        <MdLogout /> Login
                                                    </NavDropdown.Item>
                                                </LinkContainer>
                                                <LinkContainer to="/signup">
                                                    <NavDropdown.Item>
                                                        <MdOutlineAppRegistration /> Registration
                                                    </NavDropdown.Item>
                                                </LinkContainer>
                                                <NavDropdown.Divider />
                                                <LinkContainer to="/support">
                                                    <NavDropdown.Item href="">
                                                        Contact us
                                                    </NavDropdown.Item>
                                                </LinkContainer>
                                            </NavDropdown>
                                )
                            }
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </header>
    )
};

export default Header;