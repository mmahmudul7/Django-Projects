// import './App.css'

import Button from "./components/Button";

function App() {
  const handleClick = () => console.log("Button Clicked");

  return (
    <>
      {
        <Button handleClick={handleClick} color="warning">oneSix Button</Button>
      }
    </>
  );
}

export default App;