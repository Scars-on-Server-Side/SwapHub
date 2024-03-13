import { createBrowserRouter, RouterProvider } from "react-router-dom";
import StartPage from "./pages/StartPage.tsx";


function Router(props) {
  const accessToken = props.accessToken;

  const handleUnauthorized = () => { props.onUnauthorized(); }
  const handleLogout = () => { props.onLogout(); }


    const router = createBrowserRouter([
      {
        path: "/",
        element: (
          <StartPage
            accessToken={accessToken}
            onUnauthorized={handleUnauthorized}
            onLogout={handleLogout}
          />
        ),
      },
    ]);

  return <RouterProvider router={router} />;
}

export default Router;
