import "../styles/title_card_style.css";


function TitleCard({ title, description }) {
  return (
    <div>
      <div className="title-card">
        <div className="title-card-text">
          <h1>{title}</h1>
          <p>{description}</p>
        </div>
      </div>
    </div>
  );
}

export default TitleCard;
