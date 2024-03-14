import { createBrowserRouter, RouterProvider } from "react-router-dom";
import StartPage from "./pages/StartPage.tsx";
import AuthFormPage from "./pages/AuthFormPage.tsx";


function Router(props) {
  const accessToken = props.accessToken;

  const handleLogin = (formData) => {props.onLogin(formData);}
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
      {
        path: "/authform/",
        element: (
          <AuthFormPage
            onLogin={handleLogin}
          />
        ),
      },
    ]);

  return <RouterProvider router={router} />;
}

export default Router;
