import { Link } from 'react-router';

const PaymentSuccess = () => {
    return (
        <div>
            Payment success return To{' '}
            <Link to="/dashboard" className="text-pink-500">
                Dashboard
            </Link>
        </div>
    );
};

export default PaymentSuccess;
