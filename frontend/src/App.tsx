import React from "react";
import "./App.css";
import Header from "./components/header/Header.tsx";
import Start from "./components/start/Start.tsx";

import axios from "axios";
import { useState, useEffect } from "react";

function App() {
  // Define state variables for startThings and things
  const [startThings, setStartThings] = useState([{}]);
  const [things, setThings] = useState([{}]);

  // Function to fetch things data from the API
  const fetchThings = async () => {
    await axios
      .get("http://localhost:80/api/v1/thing/", {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((response) => {
        setThings(response.data);
        // Set startThings to the last 6 items of the response data
        setStartThings(response.data.slice(-6));
      })
      .catch((error) => {
        console.error(error);
        console.log(things + "things");
        console.log(startThings + "startThings");
      });
  };

  // Fetch things when component mounts
  useEffect(() => {
    fetchThings();
  }, []);

  // Function to handle avatar click
  const handleClickAvatar = () => {
    alert("Avatar clicked");
    console.log(things);
    console.log(startThings);
    console.log(things[0]);
    console.log(startThings[0]);
  };

  // Render Header and Start components with props
  return (
    <div className="App">
      <Header onClickAvatar={handleClickAvatar} />
      <Start startThings={startThings} />
    </div>
  );
}

export default App;
