import { createBrowserRouter } from "react-router-dom";
import { Root } from "../Root";
import { Login } from "../pages/Login/Login";
import { Register } from "../pages/Register/Register";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
    children: [
      {
        path: "login",
        element: <Login/>
      },
      {
        path: "register",
        element: <Register/>
      }
    ]
  }
])

export enum routes {
  login = "login",
  register = "register"
};
