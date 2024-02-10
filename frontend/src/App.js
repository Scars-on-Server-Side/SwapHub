import './App.css';
import Header from "./components/header/Header.jsx";
import Start from './components/start/Start.jsx';

import axios from "axios";
import { useState, useEffect } from 'react';


function App() {
  const [startThings, setStartThings] = useState([{}]);
  const [things, setThings] = useState([{}]);

  const fetchThings = async () => {
    await axios
      .get("http://localhost:80/api/v1/thing/", {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((response) => {
        setThings(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchThings();
      console.log(data);
      if (data !== null && data !== undefined) {
        setThings(data);
        setStartThings(data.slice(-6));
        console.log(data);
      }
    };

    fetchData();
  }, []);

  const handleClickAvatar = () => {
    alert('Avatar clicked');
  }

  return (
    <div className="App">
      <Header onClickAvatar={handleClickAvatar} />
      <Start startThings={startThings} />
    </div>
  );
}

export default App;
