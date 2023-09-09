import "./menuList.css";
// import { HTMLAttributes } from "react";
import { Item } from "./Item/Item";

type MenuListProps = {
  display: boolean;
};

export const MenuList = ( { display }: MenuListProps ) => {
  if (display) {
    return (
      <div className="menu-list">
        <Item
          itemUrl={"./src/assets/img/icons8-register-96.png"}
          linkText="войти"
          to="login"
        />
        <Item
          itemUrl={"./src/assets/img/icons8-tag-96.png"}
          linkText="поиск по тегам"
          to="login"
        />
        <Item
          itemUrl={"./src/assets/img/icons8-settings-96.png"}
          linkText="настройки"
          to="login"
        />
      </div>
    )
  }
  
  return <></>
}