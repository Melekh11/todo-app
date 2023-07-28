import "./header.css";
import { Menu } from "./Menu/Menu";
import { MenuList } from "../MenuList/MenuList";
import { useState } from "react";

export function Header() {

  const [isMenuActive, setMenuActive] = useState(false);

  const handleClickMenu = (val: boolean) => {
    console.log("change!!");
    setMenuActive(val);
  }

  return (
    <header className="header">
      <img 
        className="header__logo"
        src="./src/assets/img/icons8-todo-list-96.png"
      />
      <hr className="header__line"/>
      <h1 className="header__title">Todo App</h1>
      <hr className="header__line"/>
      <Menu onChange={handleClickMenu} children={ <MenuList display={isMenuActive} /> }/>
    </header>
  )
}
