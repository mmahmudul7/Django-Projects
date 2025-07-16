/* eslint-disable react/prop-types */
import { useState } from "react";

const List = ({ items = [], heading }) => {
    const [selectedIndex, setSelectedIndex] = useState(-1);

    return (
        <div>
            <h1 className="text-xl font-bold">{heading}</h1>
            <ul className="pl-10 list-decimal text-xl">
                {items.map((fruit, index) => {
                    return (
                        <li
                            className={
                                selectedIndex === index ? "bg-blue-500 p-3 rounded-sm m-3 text-white" : ""
                            }
                            onClick={() => setSelectedIndex(index)}
                            key={fruit}
                        >
                            {fruit}
                        </li>
                    );
                })}
            </ul>
        </div>
    );
};

export default List;