import { createBrowserRouter, RouterProvider } from "react-router-dom";
import StartPage from "./pages/StartPage.tsx";


function Router(props) {
    const accessToken = props.accessToken;

    const router = createBrowserRouter([
      {
        path: "/",
        element: <StartPage accessToken={accessToken} />,
      },
    ]);

  return <RouterProvider router={router} />;
}

export default Router;
