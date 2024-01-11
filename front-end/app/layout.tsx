import Link from "next/link";

export const metadata = {
  title: "Recipe Suggestor",
  description: "Side-Project of Bradley Hill",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <main>
          <nav>
            <Link href="/">Home</Link>
            <Link href="/login">Login</Link>
            <Link href="/ingredients">Ingredients</Link>
            <Link href="/addRecipe">Add Recipe</Link>
          </nav>
          {children}
        </main>
      </body>
    </html>
  );
}
