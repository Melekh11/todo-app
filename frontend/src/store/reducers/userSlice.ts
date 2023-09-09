import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../store";

export type UserState = {
  login: string;
  logged: boolean;
}

const initialState: UserState = {
  login: "",
  logged: false
};

export const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    login: (state, action: PayloadAction<string>) => {
      console.log("state changed");
      state.login = action.payload;
      state.logged = true;
    },
    logout: state => {
      state.login = "";
      state.logged = false;
    }
  }
});

export const {login, logout} = userSlice.actions;
export const loginSelector = (state: RootState) => state.user.login;
