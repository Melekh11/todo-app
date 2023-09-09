import { LiHTMLAttributes } from "react";
import "./item.css";
import { Link } from "react-router-dom";

type ItemProps = {
  to: string;
  itemUrl: string;
  linkText: string;
} & LiHTMLAttributes<HTMLLIElement>;

export const Item = ({ itemUrl, linkText, to }: ItemProps) => {
  return (
    <Link to={to} className="menu-list__item">
      <div className="menu-list__item-logo" style={{
        backgroundImage: `url(${itemUrl})`
      }}>
      </div>
      <p className="menu-list__item-name">{ linkText }</p>
    </Link>
  )
}