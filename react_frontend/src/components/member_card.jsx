import React from 'react';
import '../styles/member_card_style.css';

function MemberCard(props) {
  return (
    <div className="member-card">
      <img className="avatar" src={props.member.avatar} alt="avatar" />
      <h2>{props.member.name}</h2>
      <p>{props.member.email}</p>
      <p>{props.member.role}</p>
    </div>
  );
}

export default MemberCard;