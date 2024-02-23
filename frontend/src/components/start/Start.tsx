import StartThing from "./StartThing.tsx";
import axios from "axios";
import React from "react";
import { useEffect, useState } from "react";

function Start(props) {
  const startThings = props.startThings;
  const [startThingsImages, setStartThingsImages] = useState({});

  const fetchThingImage = async (thing) => {
    try {
      const response = await axios.get(
        `http://localhost:80/api/v1/thingimage/${thing.images[0]}`,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      return response.data.image;
    } catch (error) {
      console.error(error);
      return null;
    }
  };

  useEffect(() => {
    const fetchImages = async () => {
      const images = {};
      for (const thing of startThings) {
        if (thing.images && thing.images.length > 0) {
          const url = await fetchThingImage(thing);
          if (url) {
            images[thing.images[0]] = url;
          }
        }
      }
      setStartThingsImages(images);
    };
    fetchImages();
  }, [startThings]);

  return (
    <ul className="Start row row-cols-1 row-cols-md-3 g-4 m-3">
      {startThings.map((thing, index) => (
        <StartThing
          key={index}
          img={startThingsImages[thing.images[0]]}
          name={thing.name}
        />
      ))}
    </ul>
  );
}

export default Start;
