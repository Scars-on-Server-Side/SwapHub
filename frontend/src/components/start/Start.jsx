import StartThing from "./StartThing";


function Start(props) {
    const startThings = props.startThings

    return (
        <div className="Start">
            {startThings.map((thing) => (
                <StartThing key={thing.id} img={thing.img} name={thing.name} />
            ))}
        </div>
    )
}

export default Start;
