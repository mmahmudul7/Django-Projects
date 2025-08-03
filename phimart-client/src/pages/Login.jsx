import { useContext } from 'react';
import AuthContext from '../context/AuthContext';

const Login = () => {
    const { loginUser } = useContext(AuthContext);

    return (
        <div className="m-6">
            <h1>This is login page</h1>
            <button
                className="btn btn-secondary"
                onClick={() => loginUser('admin@onesix.dev', 'admin')}
            >
                Click to login
            </button>
        </div>
    );
};

export default Login;
