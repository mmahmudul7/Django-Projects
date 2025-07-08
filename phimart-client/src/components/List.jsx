const List = () => {
    const fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango', 'Pine Apple'];

    let selectedIndex = -1;
    const handleItemPrint = (index) => {
        selectedIndex = index;
        console.log(selectedIndex);
    };

    return (
        <div>
            <ul className="pl-10 list-decimal text-xl">
                {fruits.map((fruit, index) => {
                    return (
                        <li
                            className={
                                selectedIndex === index ? "bg-blue-500 p-3 rounded-sm m-3" : ""
                            }
                            onClick={() => handleItemPrint(index)}
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