import { Outlet } from "react-router-dom";
import { Footer } from "./components/Footer/Footer";
import { Header } from "./components/Header/Header";

function Root() {
  return (
    <>
      <Header/>
      <Outlet />
      <Footer/>
    </>
  )
}

export { Root };
