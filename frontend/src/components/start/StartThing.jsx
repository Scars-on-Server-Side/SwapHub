function StartThing(props) {
    const { img, name } = props;

  return (
    <li className="StartItem col mb-4">
      <div className="card h-100">
        <img src={img} alt={name} />
        <div className="card-footer">
          <small className="text-body-secondary">{name}</small>
        </div>
      </div>
    </li>
  );
}

export default StartThing;
