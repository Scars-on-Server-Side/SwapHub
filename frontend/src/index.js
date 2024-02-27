import * as React from "react";
import * as ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import StartPage from "./pages/StartPage.tsx";
import "./index.css";


const router = createBrowserRouter([
  {
    path: "/",
    element: <StartPage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
