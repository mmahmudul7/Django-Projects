import { useState } from "react";

const Skills = () => {
    const [skills, setSkills] = useState(["python", "javascript"]);

    const handleSkills = () => {
        // Add item
        // setSkills([...skills, 'React']);

        // Remove item
        // setSkills(skills.filter((item) => item != "python"));

        // Update Item 
        setSkills(
            skills.map((item) => (item == "javascript" ? (item = "React") : item))
        );
    };
    return (
        <div className="m-5">
            <ul className="m-5 list-disc">
                {skills.map((skill) => (
                    <li key={skill}>{skill}</li>
                ))}
            </ul>
            <button onClick={handleSkills}
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Handle Skill</button>
        </div>
    );
};

export default Skills;