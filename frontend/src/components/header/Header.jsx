function Header(props) {

  const handleClickAvatar = () => {
    props.onClickAvatar()
  }

  return (
    <header className="Header">
      <h1 className="Swap">
        Swap<span className="Hub">Hub</span>
      </h1>
      <img src="http://localhost:80/media/user.png" alt="avatar" onClick={handleClickAvatar} />
    </header>
  );
}

export default Header;
