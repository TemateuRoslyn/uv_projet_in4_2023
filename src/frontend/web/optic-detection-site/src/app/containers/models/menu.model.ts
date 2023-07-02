
export interface INavData {
    name?: string;
    url?: string | any[];
    href?: string;
    icon?: string;
    iconComponent?: any;
    title?: boolean;
    children?: INavData[];
    variant?: string;
    divider?: boolean;
    class?: string;
    label?: string;
}