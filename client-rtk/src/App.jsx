import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'react-toastify/dist/ReactToastify.css';
import { ToastContainer } from 'react-toastify';
import Footer from './components/Footer';
import Header from './components/Header';
import HomePage from './pages/HomePage';
import LiveDispatchPage from './pages/LiveDispatchPage';
import NotFound from './components/NotFound';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import EmployeeDashboard from './pages/Employee/EmployeeDashboard'



const App = () => {

  return (
      <Router>
        <Header />
        <main className="py-16">
          <Routes>
            <Route path="/" element={<HomePage />} />
          </Routes>
          <Routes>
            <Route path="/dispatch" element={<LiveDispatchPage />} />
            <Route path="/employee" element={<EmployeeDashboard />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/signup" element={<SignupPage />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
          <ToastContainer theme="dark" />
        </main>
        <Footer />
      </Router>
  );
}

export default App;
