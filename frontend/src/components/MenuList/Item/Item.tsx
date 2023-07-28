import { LiHTMLAttributes } from "react";
import "./item.css";

type ItemProps = {
  itemUrl: string;
  linkText: string;
} & LiHTMLAttributes<HTMLLIElement>;

export const Item = ({ itemUrl, linkText }: ItemProps) => {
  return (
    <li className="menu-list__item">
      <div className="menu-list__item-logo" style={{
        backgroundImage: `url(${itemUrl})`
      }}>
      </div>
      <p className="menu-list__item-name">{ linkText }</p>
    </li>
  )
}