// src/app/page.test.tsx

import Page from './page' // This imports your homepage component

// Simple unit test that doesn't require @testing-library. It calls the
// component function directly (which returns a React element) and extracts
// text from the returned element tree. This avoids depending on
// `@testing-library/react` and `@testing-library/jest-dom` in environments
// where those packages aren't installed.
describe('Home Page', () => {
    it('renders the heading text "Myself"', () => {
        const element = Page()

        // Recursively extract text content from a React element tree.
        function extractText(node: any): string {
            if (node === null || node === undefined) return ''
            if (typeof node === 'string' || typeof node === 'number') return String(node)
            if (Array.isArray(node)) return node.map(extractText).join('')
            if (typeof node === 'object' && node.props) return extractText(node.props.children)
            return ''
        }

        const text = extractText(element)
        expect(text).toContain('Myself')
    })
})
