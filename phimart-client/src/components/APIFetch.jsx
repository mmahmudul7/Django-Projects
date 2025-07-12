import axios from "axios";
import { useEffect, useState } from "react";

const APIFetch = () => {
    const [users, setUsers] = useState([]);

    // useEffect(() => {
    //     fetch("https://jsonplaceholder.typicode.com/users")
    //     .then((res) => res.json())
    //     .then((data) => setUsers(data));
    // }, []);

    useEffect(() => {
        axios.get("https://jsonplaceholder.typicode.com/users")
        // .then((data) => console.log(data));
        .then((data) => setUsers(data.data));
    }, []);

    return (
        <div className="m-5">
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

