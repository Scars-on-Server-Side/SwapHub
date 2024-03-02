import StartThing from "./StartThing.tsx";
import React from "react";


function Start(props) {
  const startThings = props.startThings;
  const host = props.host;


  return (
    <div className="Start">
      {startThings.map((thing, index) => (
        <StartThing
          key={index}
          img={`${host}${thing.images}`}
          name={thing.name}
        />
      ))}
    </div>
  );
}

export default Start;
