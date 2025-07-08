// import './App.css'
import FirstComponent from './components/FirstComponent';
import List from './components/List';

function App() {
  const fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango', 'Pine Apple'];
  const cities = ['Dhaka', 'Rajshahi', 'Rangpur', 'Sylhet', 'Khulna'];

  return (
    <>
      <FirstComponent />
      <List items={fruits} heading="Fruits" />
      <List items={cities} heading="Cities"></List>
    </>
  );
}

export default App;