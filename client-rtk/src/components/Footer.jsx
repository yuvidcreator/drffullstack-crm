import React from 'react'
import { Container, Col, Row } from 'react-bootstrap'

const Footer = () => {
    return (
        <footer>
            <Container>
                <div className="align-items-center justify-content-center text-center">
                    <div className="py-2">
                        Compyright &copy; Yantrayug {new Date().getFullYear()}
                    </div>
                </div>
            </Container>
        </footer>
    )
}

export default Footer