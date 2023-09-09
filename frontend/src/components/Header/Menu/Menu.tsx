import "./menu.css";
import { ChangeEvent } from "react";

type f = (val: boolean) => void;

type MenuProps = {
  onChange: f;
  children?: React.ReactNode;
};

export function Menu({ onChange, children }: MenuProps) {
  return (
    <div className="header__menu">
      <input type="checkbox" onChange={(e: ChangeEvent<HTMLInputElement>) => {

        onChange(e.target.checked);
      }}/>

      <span className="header__menu-line"/>
      <span className="header__menu-line"/>
      <span className="header__menu-line"/>

      {children}

    </div>
  )
}
