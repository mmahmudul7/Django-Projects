import axios from "axios";
import { useEffect, useState } from "react";

const APIFetch = () => {
    const [users, setUsers] = useState([]);
    const [error, setError] = useState("");

    useEffect(() => {
        axios.get("https://jsonplaceholder.typicode.com/user")
        .then((data) => setUsers(data.data))
        // .catch((err) => console.log(err));
        .catch((err) => setError(err.message));
    }, []);

    return (
        <div className="m-5">
            {error && <p className="bg-red-100 text-red-900">{error}</p>}
            <ul className="m-5 list-disc">
                {users.map((user) => (
                    <li key={user.id}>
                        {user.name}
                        <p>{user.email}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default APIFetch;

