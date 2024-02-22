import "./App.css";
import Header from "./components/header/Header.jsx";
import Start from "./components/start/Start.jsx";

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

  // Function to fetch images for each thing
  const fetchThingsImages = async () => {
    const imagesPromises = startThings.map(async (thing) => {
      if (thing.images) {
        const imagePromises = thing.images.map(async (id) => {
          try {
            const response = await axios.get(
              `http://localhost:80/api/v1/thingimage/${id}`,
              {
                headers: {
                  "Content-Type": "application/json",
                },
              }
            );
            return response.data.image; // Assume this is the image URL
          } catch (error) {
            console.error(error);
            return null;
          }
        });
        const images = await Promise.all(imagePromises);
        return { ...thing, images };
      } else {
        return thing;
      }
    });

    const updatedStartThings = await Promise.all(imagesPromises);
    setStartThings(updatedStartThings);
    console.log(updatedStartThings + "fetchThingsImages");
  };

  // Fetch things and images when component mounts
  useEffect(() => {
    fetchThings();
    fetchThingsImages();
  }, []);

  // Function to handle avatar click
  const handleClickAvatar = () => {
    alert("Avatar clicked");
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
