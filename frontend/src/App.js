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
        setStartThings(response.data.slice(-6));
      })
      .catch((error) => {
        console.error(error);
        console.log(things + "things");
        console.log(startThings + "startThings");
      });
  };

  const fetchThingsImages = (thing) => { 
    let images = [];
    thing.images.forEach(id => {
      axios
        .get(`http://localhost:80/api/v1/thingimage/${id}`, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          images.push(response.data.image);
        })
        .catch((error) => {
          console.error(error);
        });
    });
    console.log(images);
  }
  
  useEffect(() => {
    fetchThings();
    fetchThingsImages();
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
