import "./menuList.css";
// import { HTMLAttributes } from "react";
import { Item } from "./Item/Item";

type MenuListProps = {
  display: boolean;
};

export const MenuList = ( { display }: MenuListProps ) => {
  if (display) {
    return (
      <ul className="menu-list">
        <Item
          itemUrl={"./src/assets/img/icons8-settings-96.png"}
          linkText="Настройки"
        />
        <Item
          itemUrl={"./src/assets/img/icons8-tag-96.png"}
          linkText="найти по тегу"
        />
      </ul>
    )
  }
  
  return <></>
}