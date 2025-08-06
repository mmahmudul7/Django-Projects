import { Link } from 'react-router';

const Register = () => {
    return (
        <div className="flex min-h-screen items-center justify-center px-4 py-12 bg-base-200">
            <div className="card w-full max-w-md bg-base-100 shadow-xl">
                <div className="card-body">
                    <h2 className="card-title text-2xl font-bold">Sign Up</h2>
                    <p className="text-base-content/70">
                        Create an account to get started
                    </p>

                    <form className="space-y-4 mt-4">
                        <div className="form-control">
                            <label className="label" htmlFor="first_name">
                                <span className="label-text">First Name</span>
                            </label>
                            <input
                                id="first_name"
                                type="text"
                                placeholder="John"
                                className="input input-bordered w-full"
                            />
                        </div>

                        <div className="form-control">
                            <label className="label" htmlFor="last_name">
                                <span className="label-text">Last Name</span>
                            </label>
                            <input
                                id="last_name"
                                type="text"
                                placeholder="Doe"
                                className="input input-bordered w-full"
                            />
                        </div>

                        <div className="form-control">
                            <label className="label" htmlFor="email">
                                <span className="label-text">Email</span>
                            </label>
                            <input
                                id="email"
                                type="email"
                                placeholder="name@example.com"
                                className="input input-bordered w-full"
                            />
                        </div>

                        <div className="form-control">
                            <label className="label" htmlFor="address">
                                <span className="label-text">Address</span>
                            </label>
                            <input
                                id="address"
                                type="text"
                                placeholder="7/A Dhanmondi, Dhaka"
                                className="input input-bordered w-full"
                            />
                        </div>

                        <div className="form-control">
                            <label className="label" htmlFor="phone_number">
                                <span className="label-text">Phone Number</span>
                            </label>
                            <input
                                id="phone_number"
                                type="text"
                                placeholder="0123456789"
                                className="input input-bordered w-full"
                            />
                        </div>

                        <div className="form-control">
                            <label className="label" htmlFor="password">
                                <span className="label-text">Password</span>
                            </label>
                            <input
                                id="password"
                                type="password"
                                placeholder="••••••••"
                                className="input input-bordered w-full"
                            />
                        </div>

                        <div className="form-control">
                            <label className="label" htmlFor="confirmPassword">
                                <span className="label-text">
                                    Confirm Password
                                </span>
                            </label>
                            <input
                                id="confirmPassword"
                                type="password"
                                placeholder="••••••••"
                                className="input input-bordered w-full"
                            />
                        </div>

                        <button
                            type="submit"
                            className="btn btn-primary w-full"
                        >
                            Sign Up
                        </button>
                    </form>

                    <div className="text-center mt-4">
                        <p className="text-base-content/70">
                            Already have an account?{' '}
                            <Link to="/login" className="link link-primary">
                                Sign in
                            </Link>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Register;
