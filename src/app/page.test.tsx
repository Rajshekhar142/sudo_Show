// src/app/page.test.tsx
import Page from './page'

describe('Home Page', () => {
    it('renders the heading text "Myself"', () => {
        const element = Page()
        
        // Recursively extract text content from a React element tree.
        function extractText(node: unknown): string {
            if (node === null || node === undefined) return ''
            if (typeof node === 'string' || typeof node === 'number') return String(node)
            if (Array.isArray(node)) return node.map(extractText).join('')
            
            // Type guard for React elements with props
            if (
                typeof node === 'object' && 
                node !== null && 
                'props' in node && 
                typeof node.props === 'object' && 
                node.props !== null &&
                'children' in node.props
            ) {
                return extractText(node.props.children)
            }
            
            return ''
        }
        
        const text = extractText(element)
        console.log('Extracted text:', text)
        expect(text).toContain('Myself')
    })
})