import type { Metadata } from "next";
import { Jomolhari } from "next/font/google";
// import { Lexend } from "next/font/google";
import ThemeProvider from "./components/ThemeProvider";
import "./globals.css";
import './utils/colors.css'

const font = Jomolhari({ weight: "400", subsets: ["latin"] })
// const font = Lexend({ weight: "300", subsets: ["latin"] })


export const metadata: Metadata = {
  title: "Evaluation",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={font.className}>
        <ThemeProvider>
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
