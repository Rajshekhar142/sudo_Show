export type Project = {
    id: number;
    title: string;
    description: string;
    technologies: string[];
}

export const projects: Project[] = [
    {
        id: 1,
    title: 'Astra Route',
    description: 'A route prediction model using Graph Neural Networks and LightGBM to optimize delivery routes.',
    technologies: ['Python', 'GNN', 'LightGBM', 'Scikit-learn'],
    },
    {
        id: 2,
    title: 'DevOps CI/CD Pipeline',
    description: 'Automated build, test, and deployment pipeline for a containerized web application.',
    technologies: ['Docker', 'Kubernetes', 'Jenkins', 'GitHub Actions'],
    },
    {
        id: 3,
    title: 'My Personal Portfolio',
    description: 'The very site you are looking at now, built to learn and showcase Next.js.',
    technologies: ['Next.js', 'React', 'TypeScript', 'Tailwind CSS'],
    }
]